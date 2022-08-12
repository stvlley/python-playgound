class Linter

    def initialize
        # we use an array as our stack
        @stack = Stack.new
    end

    def lint(text)
        # we start the loop which reads each char in our string
        text.each_char do |char|

            # if the char is an opening brace
            if is_opening_brace?(char)
                # we push it onto the stack
                @stack.push(char)
            # if it is a closing brace
            elsif is_closing_brace?(char)

                # pop from the stack
                popped_opening_brace = @stack.pop

                # if the stack was empty, so what we popped was nil,
                # it means that an opening brace is missing:
                if !popped_opening_brace
                    return "#{char} doesn't have an opening brace"
                end

                # if the popped opening brace doesnt match the current
                # closing brace we produce an error
                if is_not_a_match(popped_opening_brace, char)
                    return "#{char} has mismatched opening brace"
                end
            end
        end

        # if we get to the end of the line, and the stack isn't empty:
        if @stack.read

            # it means we have an opening brace without a corresponding
            # closing brace, so we produce an error:
            return "#{@stack.read} does not have closing brace"
        end
        # return true if the line has no errors
        return true
    end

    private

    def is_opening_brace?(char)
        ["(", "[", "{"].include?(char)
    end

    def is_closing_brace?(char)
        [")", "]", "}"].include?(char)
    end

    def is_not_a_match(opening_brace, closing_brace)
        closing_brace != {"(" => ")", "[" => "]", "{" => "}"}[opening_brace]
    end

end
